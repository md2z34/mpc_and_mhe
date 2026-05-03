from casadi import Opti


opti = Opti()

mass_apple = opti.variable()
mass_banana = opti.variable()
opti.minimize(-700 * mass_apple - 600 * mass_banana)

area_needed = 4000 * mass_apple + 3000 * mass_banana
fertilizer_needed = 60 * mass_apple + 80 * mass_banana

opti.subject_to(mass_apple >= 0)
opti.subject_to(mass_banana >= 0)

opti.subject_to(opti.bounded(0, area_needed, 100_000))
opti.subject_to(opti.bounded(0, fertilizer_needed, 2000))

opti.set_initial(mass_apple, 5)
opti.set_initial(mass_banana, 5)

opti.solver('ipopt')

solution = opti.solve()

print(f'Mass of apples: {solution.value(mass_apple):.2f} kg')
print(f'Mass of bananas: {solution.value(mass_banana):.2f} kg')