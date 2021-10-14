from flask import Flask, render_template
from flask_sock import Sock
from flask import jsonify
import time
import random

app = Flask(__name__)
sock = Sock(app)


@sock.route("/echo")
def echo(sock):
    # update these with student points from webcam
    p_0 = {"x":0,"y":0}
    p_1 = {"x":1,"y":1}
    p_2 = {"x":2,"y":2}
    p_3 = {"x":3,"y":3}
    p_4 = {"x":4,"y":4}
    l = [p_0, p_1, p_2, p_3, p_4]
    data = {
        "P_0":p_0,
        "P_1":p_1,
        "P_2":p_2,
        "P_3":p_3,
        "P_4":p_4
    }
    print(data)
    # res = jsonify([1, 2, 3, 4, 5])
    while True:
        sock.send(data)
        for i in l:
            i["x"] = round((i["x"] + random.uniform(-1,1)) * 100) / 100
            i["y"] = round((i["y"] + random.uniform(-1,1)) * 100) / 100
        time.sleep(0.5)
        # data = sock.receive()
        # print("received", data)


app.run()
