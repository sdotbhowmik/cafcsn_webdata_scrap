1) datafile.xlsx should be empty before run the script.
2) datafile.xlsx must be closed in office program.
3) provide the required credential (email, password) in config.py
4) define the number page available in the system.
5) Run them command as follows

    #run command to get data in console along with excel
    pytest mainBOT\test_bot.py -s --maximize

    #For running operation in headless mode
    pytest mainBOT\test_bot.py -s --headless
