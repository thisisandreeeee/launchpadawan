## Automate the tedious process of uploading interviews to Launchpad Central, and delude yourself that you're going to get an A for TR4049.
![Launch Padawan Demo](https://raw.githubusercontent.com/thisisandreeeee/launchpadawan/master/demo.gif)

The script has been tested to work with Python 2.

First up, let's figure out what OS you're on. If you're on Windows, you're on your own buddy. If you're on OSX, great job! Edit the following code block, and enter it into your terminal to get started.
```
git clone https://github.com/thisisandreeeee/launchpadawan.git /path/to/desired/directory
cd /path/to/desired/directory
pip install -r requirements.txt
echo "USERNAME='your launchpad email address'\nPASSWORD='your launchpad password'" >> settings.py
wget http://chromedriver.storage.googleapis.com/2.25/chromedriver_mac64.zip
unzip chromedriver_mac64.zip
rm chromedriver_mac64.zip
```
If you're on linux, well, figure it out.

### Show me how to win at life
If you have a bunch of interviews that you want to add, but are too lazy and annoyed to bother navigating an abhorent wasteland that is the launchpad UX, boy will this script help. You will still have to phrase your survey results in terms of the Key Insights, and Interview Description - what this script cannot do is paraphrase your survey results into something the LLC accepts. This is automation, not magic.

To get started, open up `sample.json` in ~~vim~~ your text editor of choice. It kinda looks a little like this:
```
[
    {
        "email": "linus.torvald@hotmale.com",
        "role": "The Rootfather",
        "date": "12-18-2016", 
        "insights": "This is NOT a summary of your interaction. This is the 'A-Ha! Moment' you experienced.",
        "description": "A good framework to follow here is: What we thought before this meeting. What we learned from this meeting. What we are doing next as a result of this meeting.",
        "hypotheses": [
            [hypothesis_id_1, action_id_1],
            [hypothesis_id_2, action_id_2]
        ]
    }
]
```
It's all pretty intuitive. But wait, what is this I see as the value of the `hypotheses` key? It accepts a list of lists, with the inner lists containing information on the hypothesis ID, and action ID.

#### How to obtain the hypothesis ID
1. Open your LLC, and click on Add New, followed by Customer Interview
2. Scroll all the way down to the section where you select hypotheses to validate / invalidate.
3. Inspect the element of the input checkbox. The value of the checkbox is your hypothesis ID, which is `924337` in this particular scenario.
![Hypothesis ID](https://raw.githubusercontent.com/thisisandreeeee/launchpadawan/master/Hypothesis%20ID.png)

#### How to obtain the action ID
There are 3 possible values for the action ID.
- `1` is for Don't Care
- `2` is for Nice to have
- `3` is for Must Have

Change the action IDs according to whether you would like to validate / invalidate that particular hypothesis.

### In my nutshell
When you're done, save `sample.json` and you should be good to go. Remember, the purpose of this script is simply to do away with the burden of navigating crappy UX. It does not make it any easier to consolidate the insights and learning points from the surveys or interviews you have done. Have fun.
```
python poster.py
```

### Developer Notes
If you're interested in modifying the script, all you really need to know is the `Selenium` library, and how to find the xpath of a web element. Feel free to contact me with any questions you might have.
