'''
This is a docstring - it is a way for us to leave notes in our code that take up multiple lines
Docstrings are typically used to describe what a function does or what a file is for

WELCOME TO THE TUTORIAL!
This tutorial will teach you how to use python to interact with the nft inspect api as a way to learn about python and interacting with APIs
APIs are a way for us to interact with other applications and get data from them
They are a very powerful tool that can be used to do all sorts of things and are core to the way that modern applications are built

In this tutorial we will be using the nft inspect api to get data about nft collections
instead of using the twitter API, since this would require everyone getting their own keys and tokens

In the future I will show you all how to setup your own twitter keys and use the twitter api
directly to get metrics about your tweets, but if you don't want to wait you can investigate too!

In this example we will be getting the members of a collection and their info from the nft inspect api
which will tell us things about their twitter project relevance and other things!

I will explain line by line what's happeneing - but having gone through the intro to python above will help!
'''

import requests
import pandas as pd

'''
For starters lets talk about the import statements at the top of the file
These are the libraries we are using to make our code work

We are using the requests library to make http requests to the nft inspect api
We are using the pandas library to make our data look nice in a table

You can install these libraries by running the following commands in your terminal
pip install requests
pip install pandas

API = Application Programming Interface
This is a way for us to interact with other applications and get data from them
In this case we are using the nft inspect api to get data about nft collections
'''

# this is a variable that will store the name of the collection we want to get data for
# you notice this is a different way of commenting than before - this is a comment that is on a single line
# this is a string - a type of data that is used to store text


collection_name = "y00ts"

# this is an empty data frame that we will use to store the data we get from the api
# you can think of a data frame as a table


# this is a function defition - it will take input of a collection name and return the members of that collection
def get_collection_members(collection):
    '''
    Functions are what we use to accomplish programatic tasks in python
    They are defined using the def keyword and then the name of the function
    In this case we are defining a function called get_collection_members
    This function will take input of a collection name and return the members of that collection

    Functions are the building blocks of python programs and understanding them is key to writing good code
    Encompassed in the function is variables and commands structured in a way to accomplish a task
    Python is an interpreted language which means that it reads the code line by line and executes it
    This means that the code in a function is only executed when the function is called
    and it also means that we don't need to worry about defining variables types or anything like that
    Python will figure it out for us! Order matters though, so make sure you define variables before you use them
    '''

    # response is a variable that we are defining in order to hold the response from the nft inspect api
    response = requests.get(
        f"https://www.nftinspect.xyz/api/collections/members/{collection}?limit=7500&onlyNewMembers=false"
    )
    '''
    The core interactions in API handling are GET and POST requests
    GET requests are used to get data from an API
    POST requests are used to send data to an API

    Above we've used a GET request to get the members of a collection from the nft inspect api
    The url that we have passed to the get function is the url of the api endpoint that we want to hit
    The url is made up of the base url of the api (https://www.nftinspect.xyz/api) and the endpoint we want to hit (/collections/members/{collection})
    An endpoint is a specific url that is used to interact with a specific part of an API
    The collection name is passed to the function as a parameter and is used to fill in the {collection} part of the endpoint url
    The limit and onlyNewMembers parameters are also passed to tell the api how many members we want to get and whether we want to get ONLY new members or not
    '''
    if response.status_code != 200:
        raise Exception(
            "Cannot get user data (HTTP {}): {}".format(
                response.status_code, response.text)
        )
    '''
    The function above is a conditional statement that will raise an exception if the response status code is not 200
    status codes are a way for us to know if our request was successful or not - 200 means that the request was successful
    400 means that the request was bad and 500 means that there was an error on the server side
    to access the status code of the response - we need to access it's member variable called status_code - this is done using the . operator
    again - we don't need to define any types for the variables we are using - python will figure it out for us!
    if you had to guess based on the intro to python above, what types do you think we're using?

    json is a data format that is used to store data in a key value pair format - it is very similar to a python dictionary - which is what we are using to store the response data
    the text member variable of the response object is the raw text of the response - this is typically a json string
    strings are a type of data that is used to store text - they are defined using either single or double quotes

    the .format() function is a way to format strings - it takes in a string and then the values that you want to insert into the string
    this is a way that we can use placeholders in our strings and then insert the values we want into the placeholders - {} is a placeholder
    '''

    output = response.json()
    members = output["members"]

    '''
    We first need to store the json output from the api response - we do this by using the json() function on the response object
    this will convert the json string into a python dictionary and store it in the output variable
    we then access the members key of the output dictionary and store it in the members variable
    '''

    '''
    Then we create a data frame to store the data we want to get from the api - initialize it as empty and tell it what data we want to store
    the api will return tons of data but we only want to track some aspects of it
    once we have the data we want we can then use it to do things like create a leaderboard
    first we need to store it in a data frame though - you can think of a data frame as a table
    we are using the pandas library to create the data frame - pandas is a library that is used to do data analysis and manipulation
    '''

    members_data_frame = pd.DataFrame(
        {
            "Name": [],
            "Wearing PFP": [],
            "PFP URL": [],
            "Global Reach": [],
            "Rank": [],
            "Time With Token": [],
            "Time With Collection": [],
        }
    )

    '''
    We are then looping through the members list and printing out the member dictionary - this will hold all relevant data for each member
    the for loop is defined using the for keyword and then the variable that we want to use to store the current item in the list
    member is the variable that we are using to store the current member dictionary from the members dictionary list
    we are then accessing the keys of the member dictionary and storing them in variables - we've chosen relevant data but you can access any data you want
    just uncomment the print statement on line 90 and run the code to see what the member dictionary looks like - try it out!
    alternatively you can use the nft inspect api explorer to see what data is available for each endpoint
    another option is to print output on line 87 with a print statement - try it out!
    '''

    for member in members:
        # print("Member :", member, "\n")
        member_name = member["name"]
        member_wearing_pfp = member["isWearingCollectionsPfp"]
        member_pfp_url = member["pfpUrl"]
        member_global_reach = member["globalReach"]
        member_rank = member["rank"]
        member_time_with_token = member["timeWithToken"]
        member_time_with_collection = member["timeWithCollection"]

        member_data_frame = pd.DataFrame(
            {
                "Name": [member_name],
                "Wearing PFP": [member_wearing_pfp],
                "PFP URL": [member_pfp_url],
                "Global Reach": [member_global_reach],
                "Rank": [member_rank],
                "Time With Token": [member_time_with_token],
                "Time With Collection": [member_time_with_collection],
            }
        )

        # this line of code is adding the member data frame to the members data frame
        # this is done by using the concat function from the pandas library
        # the concat function takes in a list of data frames and then concatenates them together
        # this is a way to add rows to a data frame
        # it is inside a for loop so we are adding a row for each member for the collection from the api

        members_data_frame = pd.concat([members_data_frame, member_data_frame])

    print(members_data_frame)

    '''
    the return keyword is used to return a value from a function - this signifies that the function has finished executing
    if we set any  variable equal to this function name - it will hold the members from the collection that we pass as input
    '''

    return members

    '''
    you can see that members is set equal to the function call - this means that members will hold the value that is returned from the function
    it is currently grayed out because we are not using it - but you can uncomment add a print statemtn or do some logic with it

    the main function is a function that is used to run the code in the file
    we capture all of the code that we want to run in the main function
    this is a common pattern in python and is used to keep the code organized
    any code outside of this function will not be run - unless the function is called inside of main - which we are doing on line 131
    these comments are grayed out because they are after the return statement - this means that they will not be run
    any code in the function after the return statement will not be run
    '''


def main():
    members = get_collection_members(collection_name)


'''
the code above is a simple example of how to use the nft inspect api to get the members of a collection
and since we have defined the main function the only thing left to do is run it!
'''

main()
