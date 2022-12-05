# training
Training Freshers

# Top 500 trending projects in Github
https://api.github.com/search/repositories?sort=stars&order=desc&q=created%3A%3E2022-11-01&per_page=100&page=1


# PostgreSQL in Docker

docker run --name postgresql -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=github -p 5432:5432 -v /Users/saisyam/work/postgresql_data:/var/lib/postgresql/data -d postgres