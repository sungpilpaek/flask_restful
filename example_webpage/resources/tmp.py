from flask import Flask


@app.teardown_appcontext
def tmp():
    print "BYEBYE!"