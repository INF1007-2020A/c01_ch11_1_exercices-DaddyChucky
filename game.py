"""
Chapitre 11.1

Classes pour représenter un personnage.
"""

import random

import utils
UNARMED_POWER = 20


def make_unarmed():
	return Weapon("Unarmed", UNARMED_POWER, 1)


class Weapon:
	def __init__(self, name, power, min_level):
		self.name = name
		self.power = power
		self.min_level = min_level


class Character:
	def __init__(self, name, hp, attack, defense, level, weapon=make_unarmed()):
		self.name = name
		self.hp = hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = weapon

	def compute_damage(self, defender: "Character") -> tuple:
		random_float = random.random()
		if random_float < 0.0625:
			crit = 2
		else:
			crit = 1
		modifier = crit * random.randrange(85, 100) / 100

		return (((2/5 * self.level + 2) * self.weapon.power * self.attack / defender.defense) / 50 + 2) * modifier, crit

	def deal_damage(self, defender: "Character"):
		damage = Character.compute_damage(self, defender)
		defender.hp -= damage[0]
		if defender.hp < 0:
			defender.hp = 0
		print(f"{self.name} used {self.weapon.name}")
		if damage[1] == 2:
			print("  Critical hit!")
		print(f"{defender.name} took {round(damage[0],2)} DMG\n{defender.name} has now {round(defender.hp,2)} HP")


def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	tours = 0
	attacker = c1
	defender = c2
	print(f"{attacker.name} starts a battle with {defender.name}!")
	while True:
		# TODO: Appliquer l'attaque
		attacker.deal_damage(defender)


		# TODO: Si le défendeur est mort
		if defender.hp == 0:
			print(f"{defender.name} is sleeping with the fishes.")
			break
		if tours % 2 == 0:
			attacker = c2
			defender = c1
		else:
			attacker = c1
			defender = c2

		tours += 1
	return tours
	# TODO: Retourner nombre de tours effectués
