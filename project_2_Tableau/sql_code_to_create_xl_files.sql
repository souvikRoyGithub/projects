/*
Queries used for Tableau Project
*/
select * from project_1_2022_10_25.coviddeaths;


--  1. 

Select SUM(new_cases) as total_cases, SUM(cast(new_deaths as float)) as total_deaths, SUM(cast(new_deaths as float))/SUM(New_Cases)*100 as DeathPercentage
From project_1_2022_10_25.coviddeaths
where continent is not null
order by 1,2;



--  2. 


Select location,SUM(cast(new_deaths as float)) as TotalDeathCount
From project_1_2022_10_25.coviddeaths
Where continent is not null 
and location not in ('World', 'European Union', 'International')
Group by location
order by TotalDeathCount desc
limit 10;


--  3.

Select Location, Population, MAX(total_cases) as HighestInfectionCount,  Max((total_cases/population))*100 as PercentPopulationInfected
From project_1_2022_10_25.CovidDeaths
Where continent is not null 
and location not in ('World', 'European Union', 'International')
Group by Location, Population
order by PercentPopulationInfected desc;


--  4.


Select Location, Population,date, MAX(total_cases) as HighestInfectionCount,  Max((total_cases/population))*100 as PercentPopulationInfected
From project_1_2022_10_25.CovidDeaths
Where continent is not null 
and location not in ('World', 'European Union', 'International')
Group by Location, date
order by location;


