""" A fun exercise using vectors and points """

from projectile import Projectile
from environment import Environment
from rtmath.point import Point
from rtmath.vector import Vector
from rtmath.color import Color
from canvas import Canvas


class FunExercise:

    @staticmethod
    def run():
        p = Projectile(Point(0, 1, 0), Vector(1, 1.8, 0).normalize() * 11.25)
        e = Environment(Vector(0, -0.1, 0), Vector(-0.01, 0, 0))
        canvas = Canvas(900, 500)
        while p.position.y > 0:
            p = FunExercise.tick(e, p)
            canvas.write_pixel(
                p.position.x, 
                canvas.height - p.position.y,
                Color(1, 0, 0))
        f = open('fun_test.ppm', 'a')
        f.write(canvas.to_ppm())
        f.close()

    @staticmethod
    def tick(env, proj):
        position = proj.position + proj.velocity
        velocity = proj.velocity + env.gravity + env.wind
        return Projectile(position, velocity)


if __name__ == '__main__':
    FunExercise.run()
