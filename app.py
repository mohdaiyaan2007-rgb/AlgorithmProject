from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

def bubble_sort(arr):
    start = time.time()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return time.time() - start

def merge_sort(arr):
    start = time.time()

    def merge(arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

            merge(L)
            merge(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]; i+=1
                else:
                    arr[k] = R[j]; j+=1
                k+=1

            while i < len(L):
                arr[k] = L[i]; i+=1; k+=1
            while j < len(R):
                arr[k] = R[j]; j+=1; k+=1

    merge(arr)
    return time.time() - start

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/compare', methods=['POST'])
def compare():
    data = request.json['numbers']
    arr = list(map(int, data.split(',')))

    b = bubble_sort(arr.copy())
    m = merge_sort(arr.copy())

    return jsonify({
        "bubble": b,
        "merge": m
    })

if __name__ == '__main__':
    app.run(debug=True)