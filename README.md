# twangle
Mangles the profile photo of a certain twitter account

# Dependencies
This uses the `wand` library, so you may need to install imagemagick if you don't have it already. I should really check that. 
Also you need all the dependencies in the Pipfile... but just use pipenv and you never need to check those

You'll also need api keys for the twitter API in .env! The vars should be called `CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET`. 

# Usage
Pls use pipenv and ```pipenv install``` instead of setting up dependencies like a fool

Then run ```pipenv run python twangle.py <mangle amt> <twitter screen name>```

The output file will be saved to the main directory

have fun!

