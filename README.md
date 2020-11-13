(In progress) ray tracer implemenation

Render beautiful scenes using the [ray tracing](https://en.wikipedia.org/wiki/Ray_tracing_(graphics)) technique.

install instructions:

1. clone/download source
2. cd into source dir
3. create a virtual environment: python3 -m venv venv/ray-env
4. source venv/ray-env/bin/activate
5. pip install -e .
6. python3 -m unittest discover -s ./test/*
7. python3 fun_exercise.py 

current output:

Launch a projectile based on position, velocity, gravity, wind direction

```
x: 0.7071067811865475, y: 1.7071067811865475, z: 0.0
x: 1.404213562373095, y: 2.314213562373095, z: 0.1
x: 2.0913203435596426, y: 2.821320343559642, z: 0.30000000000000004
x: 2.7684271247461902, y: 3.2284271247461898, z: 0.6000000000000001
x: 3.4355339059327377, y: 3.5355339059327373, z: 1.0
x: 4.092640687119285, y: 3.7426406871192848, z: 1.5
x: 4.739747468305833, y: 3.849747468305832, z: 2.1
x: 5.37685424949238, y: 3.85685424949238, z: 2.8
x: 6.003961030678928, y: 3.7639610306789275, z: 3.5999999999999996
x: 6.621067811865475, y: 3.571067811865475, z: 4.5
x: 7.228174593052023, y: 3.2781745930520225, z: 5.5
x: 7.82528137423857, y: 2.88528137423857, z: 6.6
x: 8.412388155425118, y: 2.3923881554251176, z: 7.8
x: 8.989494936611665, y: 1.7994949366116653, z: 9.1
x: 9.556601717798213, y: 1.1066017177982128, z: 10.5
x: 10.11370849898476, y: 0.3137084989847604, z: 12.0
x: 10.660815280171308, y: -0.579184719828692, z: 13.6      
```
