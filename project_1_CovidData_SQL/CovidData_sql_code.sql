-- selecting data that we are going to use
SELECT continent,location,str_to_date(date,"%d-%m-%Y") as date,total_cases,new_cases,total_deaths,population FROM project_1_2022_10_25.coviddeaths 
where continent is not null order by continent,location,str_to_date(date,"%d-%m-%Y");

-- looking at 'total cases vs total death' percentage of countries
select location,sum(total_cases) as "Total cases",sum(total_deaths) as "Total deaths",(sum(total_deaths)/sum(total_cases))*100 as "percentage_of_death",population 
FROM project_1_2022_10_25.coviddeaths where continent is not null group by location order by percentage_of_death desc;

-- likelihood of dying due to covid in india
select location,sum(total_cases) as "Total cases",sum(total_deaths) as "Total deaths",(sum(total_deaths)/sum(total_cases))*100 as "percentage_of_death",population 
FROM project_1_2022_10_25.coviddeaths where continent is not null group by location having location like "india";

-- looking at infection rate of countries
select location,sum(total_cases) as "Total cases",population,(sum(total_deaths)/population)*100 as "infection_rate"
FROM project_1_2022_10_25.coviddeaths where continent is not null group by location order by infection_rate desc;

-- looking at highest infection rate of countries
select location,max(total_cases) as "Highest_infected",population,(max(total_cases)/population)*100 as "highest_infection_rate"
FROM project_1_2022_10_25.coviddeaths where continent is not null group by location order by highest_infection_rate desc;

-- looking countries highest death count per population
select location,max(cast(total_deaths as decimal)) as "Highest_death",population
FROM project_1_2022_10_25.coviddeaths where continent is not null group by location order by highest_death desc;

-- looking continents highest death count per population
select continent,max(cast(total_deaths as decimal)) as "Highest_death",population
FROM  project_1_2022_10_25.coviddeaths where continent is not null group by continent order by highest_death desc;

-- death percentage by date
select str_to_date(date,"%d-%m-%Y") as date,sum(new_cases) as cases,sum(cast(new_deaths as double)) as death,(sum(cast(new_deaths as double))/sum(new_cases))*100 as death_percentage
FROM  project_1_2022_10_25.coviddeaths where continent is not null group by date order by str_to_date(date,"%d-%m-%Y") desc;

-- looking at percentage of vaccinated people in the population by location
select dea.location,max(cast(vac.people_vaccinated as decimal)) as Total_people_vaccinated,dea.population,(max(cast(vac.people_vaccinated as decimal))/dea.population)*100  as percentage_of_people_vaccinated 
from coviddeaths dea 
inner join covidvaccinations vac on (dea.location=vac.location and dea.date=vac.date) group by dea.location order by percentage_of_people_vaccinated desc;

-- or 
select dea.location,sum(cast(vac.new_vaccinations as decimal)) as Total_people_vaccinated,
dea.population,(sum(cast(vac.new_vaccinations as decimal))/dea.population)*100  as percentage_of_people_vaccinated 
from coviddeaths dea 
inner join covidvaccinations vac on (dea.location=vac.location and dea.date=vac.date) group by dea.location order by percentage_of_people_vaccinated desc;

-- using CTE
with tempTab as (select dea.location,max(cast(vac.people_vaccinated as decimal)) as Total_people_vaccinated,dea.population,
(max(cast(vac.people_vaccinated as decimal))/dea.population)*100  as percentage_of_people_vaccinated
from coviddeaths dea 
inner join covidvaccinations vac on (dea.location=vac.location and dea.date=vac.date) group by dea.location order by percentage_of_people_vaccinated desc)
select location,Total_people_vaccinated,population,percentage_of_people_vaccinated,if(percentage_of_people_vaccinated>100 or percentage_of_people_vaccinated is null,"Data is not right","OK") as comments
from tempTab;
