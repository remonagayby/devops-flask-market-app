# this file is responsible for executing the app

from market import app

# check if the run.py file is executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True)