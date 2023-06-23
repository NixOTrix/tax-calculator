# tax-calculator

This was a coding challenge and an attempt at a flex, not necesseeraily a good program

I used this site as a refrence for the threshold tables https://www.superguide.com.au/how-super-works/income-tax-rates-brackets

To use the tool please run:

Command line:

```
docker-compose build commandLine
docker-compose run commandLine
```

API:

```
docker-compose build api
docker-compose up api
```

sample api call:

```
curl --location --request GET 'http://0.0.0.0:8080/taxcalculator' \
--header 'Content-Type: application/json' \
--data-raw '{
    "year": "2020",
    "income": "85000"
}'
```

NOTE: when prompted for the year, pick the first year in the split, ie. the 2022-2023 financial year would be listed as 2022

To run the front-end you will also need to run the api, luckily you can do so with these easy commands

```
docker-compose build frontend api
docker-compose up -d frontEnd api
```