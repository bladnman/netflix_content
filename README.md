# Netflix Content

A dataset found on Kaggle under the
name [Netflix TV and Movies](https://www.kaggle.com/datasets/victorsoeiro/netflix-tv-shows-and-movies).

A related dataset can be found
[Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows) which contains
a great [notebook for visualizations](https://www.kaggle.com/code/joshuaswords/netflix-data-visualization).

# Netflix - TV Shows and Movies

This data set was created to list all shows available on Netflix streaming, and analyze the data to find interesting
facts. This data was acquired in May 2022 containing data available in the United States.

## Content

This dataset has two files containing the titles (titles.csv) and the cast (credits.csv) for the title.

This dataset contains +5k unique titles on Netflix with 15 columns containing their information, including:

### Titles

| Field           | Description                                  |
|-----------------|----------------------------------------------| 
| id              | The title ID on JustWatch                    |
| title           | The name of the title                        |
| type            | TV show or movie                             |
| description     | A brief description                          |
| release_year    | The release year                             |
| age certification | The age certification                        |
| runtime         | The length of the episode (SHOW) or movie    |
| genres          | A list of genres                             |
| production_countries | A list of countries that produced the title  |
| seasons         | Number of seasons if it's a SHOW             |
| imdb_id         | The title ID on IMDB                         |
| imdb_score      | Score on IMDB                                |
| imdb_votes      | Votes on IMDB                                |
| tmdb_popularity | Popularity on TMDB                           |
| tmdb_score      | Score on TMDB                                |

And over +77k credits of actors and directors on Netflix titles with 5 columns containing their information, including:

### Credits

| Field          | Description                                  |
|----------------|----------------------------------------------|
| person ID      | The person ID on JustWatch |
| ID             | The title ID on JustWatch |
| name           | The actor or director's name |
| character name | The character name |
| role           | ACTOR or DIRECTOR |

Tasks
Developing a content-based recommender system using the genres and/or descriptions.
Identifying the main content available on the streaming.
Network analysis on the cast of the titles.
Exploratory data analysis to find interesting insights.
