# UrlShortener readme
### Introduction
A Fullstack web app for shortening URLs

### Project Support Features

* Users can shorten urls
* Redirects to the original links
### Installation Guide
To run this project you will need python installed on your machine first then:

* Clone the repo:

        git clone https://github.com/YasserRohaim/UrlShortener

* Install the app's dependencies:

        pip install -r requirements.txt
### Usage
* Run python manage.py runserver to start the server.
* open the website on port 8000
### API Endpoints
| HTTP Verbs | Endpoints | Action |

| GET | /shorten | presents the home page where you can enter the original URL |

| POST | /shorten | shortens the url and returns the short version |

| GET | /:short_url | redirects to the original URL |

### License
This project is available for use under the MIT License.
