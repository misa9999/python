import random
import string


# integer = random.randint(10, 20)
# integer = random.randrange(900, 1000, 10)

# floating = random.uniform(10, 20)
# floating = random.random()

# li = ["misa", "lucy", "yuuki", "megumin"]

# raffle = random.choices(li, k=2)
# raffle = random.sample(li, 2)
# random.shuffle(li)


# print(raffle)

letters = string.ascii_letters
digits = string.digits
characters = "!@#$%&*._-"
general = letters + digits + characters
passwd = "".join(random.choices(general, k=20))


print(passwd)
