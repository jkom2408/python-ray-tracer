from projectile import Projectile
from environment import Environment
from tuple.tuple import Tuple

class FunExercise:

    @staticmethod
    def run():
        p = Projectile(Tuple.point(0, 1, 0), Tuple.vector(1, 1, 0).normalize())
        e = Environment(Tuple.vector(0, -0.1, 0), Tuple.vector(-0.01, 0, 0.1))
        r = None
        while r is None or r > 0:
            p = FunExercise.tick(e, p)
            r = p.position.y
            print(f'x: {p.position.x}, y: {p.position.y}, z: {p.position.z}')

    @staticmethod
    def tick(env, proj):
        position = proj.position + proj.velocity
        velocity = proj.velocity + env.gravity + env.wind
        return Projectile(position, velocity)

if __name__ == '__main__':
    FunExercise.run()
