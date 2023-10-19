SELECT * FROM project_2_2023_01_03.`nashville_housing_data`;

-- 1> standardize date format 

	-- checking....
    
SELECT SaleDate,replace(replace(SaleDate,",","")," ","-"),str_to_date(replace(replace(SaleDate,",","")," ","-"),"%M-%d-%Y")
FROM project_2_2023_01_03.`nashville_housing_data`;

	-- converting....
    
update nashville_housing_data
set SaleDate=str_to_date(replace(replace(SaleDate,",","")," ","-"),"%M-%d-%Y");

-- 2> populate property address data ## no null value in the DB 

SELECT propertyAddress FROM project_2_2023_01_03.`nashville_housing_data`
where propertyAddress is null;

-- 3> breaking out address into individual column

		-- propertyAddress
        
	-- checking.... **charindex() is not working so have to do it manually
    
SELECT propertyAddress,substring(propertyAddress,1,length(substring_index(propertyAddress,',',1))) as Area ,
substring(propertyAddress,length(substring_index(propertyAddress,',',1))+2,length(propertyAddress)) as City
FROM project_2_2023_01_03.`nashville_housing_data`;

	-- adding and updating  the columns
    
alter table nashville_housing_data 
add column Area varchar(50) after propertyAddress,
add column City varchar(50) after Area;

update nashville_housing_data
set Area=substring(propertyAddress,1,length(substring_index(propertyAddress,',',1))),
City= substring(propertyAddress,length(substring_index(propertyAddress,',',1))+2,length(propertyAddress));

		-- ownerAddress
        
	-- checking....
    
SELECT ownerAddress FROM project_2_2023_01_03.`nashville_housing_data`;

SELECT ownerAddress,substring(ownerAddress,1,length(substring_index(ownerAddress,',',1))) as Owner_Area,
substring(ownerAddress,length(substring_index(ownerAddress,',',1))+2,length(substring_index(ownerAddress,',',2))-length(substring_index(ownerAddress,',',1))-1) as Owner_City,
substring(ownerAddress,length(substring_index(ownerAddress,',',2))+2,length(ownerAddress)) as Owner_Location
FROM project_2_2023_01_03.`nashville_housing_data`;

	-- adding and updating the columns
    
alter table nashville_housing_data 
add column Owner_Area varchar(50) after ownerAddress,
add column Owner_City varchar(50) after Owner_Area,
add  column Owner_Location varchar(50) after Owner_City;

update nashville_housing_data
set Owner_Area=substring(ownerAddress,1,length(substring_index(ownerAddress,',',1))),
Owner_City=substring(ownerAddress,length(substring_index(ownerAddress,',',1))+2,length(substring_index(ownerAddress,',',2))-length(substring_index(ownerAddress,',',1))-1),
Owner_Location=substring(ownerAddress,length(substring_index(ownerAddress,',',2))+2,length(ownerAddress));

SELECT ownerAddress,Owner_Area,Owner_City,Owner_Location FROM project_2_2023_01_03.`nashville_housing_data`;

-- 4> change Yes and No to Y and N in SoldAsVacant 

	-- checking....
    
select distinct(SoldAsVacant) from project_2_2023_01_03.nashville_housing_data;

select SoldAsVacant,
(case
when SoldAsVacant= "Yes" or SoldAsVacant="Y" then "Y"
when SoldAsVacant= "No" or SoldAsVacant= "N" then "N"
else null
end) as SoldAsVacant_edited from project_2_2023_01_03.`nashville_housing_data`;

-- adding and updating column

alter table nashville_housing_data
add column SoldAsVacant_edited varchar(3) after SoldAsVacant;

update nashville_housing_data
set SoldAsVacant_edited=(case
when SoldAsVacant= "Yes" or SoldAsVacant="Y" then "Y"
when SoldAsVacant= "No" or SoldAsVacant= "N" then "N"
else null
end);

select distinct(SoldAsVacant_edited) from project_2_2023_01_03.nashville_housing_data;

-- 5> Remove duplicates

-- checking....

with CTE as (
select * , row_number() over( 
partition by ParcelID,LandUse,PropertyAddress,SaleDate,SalePrice,LegalReference,SoldAsVacant,OwnerName,OwnerAddress,TaxDistrict,LandValue,BuildingValue,TotalValue,YearBuilt,Bedrooms,FullBath,HalfBath
order by ParcelID) as Row_num
from project_2_2023_01_03.nashville_housing_data)
select * from CTE
where Row_num>1
;

-- deleting duplicates....

delete from nashville_housing_data
where UniqueID in(with CTE as (
select * , row_number() over( 
partition by ParcelID,LandUse,PropertyAddress,SaleDate,SalePrice,LegalReference,SoldAsVacant,OwnerName,OwnerAddress,TaxDistrict,LandValue,BuildingValue,TotalValue,YearBuilt,Bedrooms,FullBath,HalfBath
order by ParcelID) as Row_num
from project_2_2023_01_03.nashville_housing_data)
select UniqueID from CTE
where Row_num>1
);

-- 6> Delete unused columns : OwnerAddress,TaxDistrict,PropertyAddress,SaleDate

alter table nashville_housing_data
drop column OwnerAddress,
drop column TaxDistrict,
drop column PropertyAddress,
drop column SaleDate;

-- done

select * from project_2_2023_01_03.nashville_housing_data;