# Web Scraping - Mission to Mars
For this assignment, we were instructed to scrap specific pieces of information from several sites related to Mars. Once this is done, we are suppose to create a scrape function and render a template to, finally, present it in a html.
The assignment was divides into two sections:
*Scrapping
*Mongo DB and Flask Application.

Both this sections are contained in:
*A jupyter notebook file
*An app.py 
*An python file that containes the scrape function
*A html file.

## Step 1 - Scraping
In this section, we were required to scrap several pages, each in a differente way in order to obtain the data.

### NASA Mars News
In the first one, I used splinter. I went into the div section that contained the first news and extract both the header and the paragraph.
![alt text](https://github.com/anajuarezar/Mission-to-Mars/blob/main/Missions_to_Mars/Screenshots/HTML_1_crop.png)

### JPL Mars Space Images - Featured Image
This second one was a litle trickier, I had to extract the source code to an image and create the url for it. I, again, used splinter and created the path to the image. Then y extracted the code, assigned to a variable and then I created the url.

![alt text](https://github.com/anajuarezar/Mission-to-Mars/blob/main/Missions_to_Mars/Screenshots/ft_image.png)


### Mars Facts
In Mars Facts, I used pandas. This was relatibly simple since I only used pandas to read the url, extract the tables it contained, choose the one I wanted and then converted it to html.

![alt text](https://github.com/anajuarezar/Mission-to-Mars/blob/main/Missions_to_Mars/Screenshots/mars_facts.png)

### Mars Hemispheres
This last section was considerably more difficult. In order to complete it, I used splinter to set up the url. Then I created an empty list and chose the first part of the path to the images. Since this was inside another web page, I created a loop that first obtained the title of the image in the main page, then went into the download page. There I constructed the path to the src code and append all to the list. Since it was a different page, I had to use beautiful soup on this page again. 


![alt text](https://github.com/anajuarezar/Mission-to-Mars/blob/main/Missions_to_Mars/Screenshots/hemispheres.png)



## Step 2 - MongoDB and Flask Application
This section was divided into three:
*The scrape function.
*The app
*The HTML

### The scrape function
This one was tricky. I first defined the function and inside I used the code I had written for scrapping. Since it could have errors I used several times the TRY statment. The results were cointained in a list. 

### The app
When I created the app that first ran the scrape code and then created a DB in Mongo I could access lated. This code linked the function and the html while creating a DB in mongo.

### The HTML
Finally the html presented the results using the mongo db we created. I was able to extract the specific information of each element because it worked as a dictionary. I used cards to show the images and the grid for the display of elements 
