import random

class Event:
    def random_productivity(self, employees):
        event_roll = random.randint(1, 100)

        bad_texts = [
            "RANDOM EVENT: The AC is broken! Productivity decreased.",
            "RANDOM EVENT: Internet outage! Productivity decreased.",
            "RANDOM EVENT: Surprise meeting added! Productivity decreased.",
            "RANDOM EVENT: Coffee machine malfunction! Productivity decreased.",
            "RANDOM EVENT: Power fluctuation! Productivity decreased.",
            "RANDOM EVENT: Office too noisy! Productivity decreased."
        ]

        good_texts = [
            "RANDOM EVENT: Free coffee & donuts! Productivity increased.",
            "RANDOM EVENT: Early dismissal announced! Productivity increased.",
            "RANDOM EVENT: Team lunch provided! Productivity increased.",
            "RANDOM EVENT: Bonus incentives given! Productivity increased.",
            "RANDOM EVENT: Comfortable workspace upgrade! Productivity increased.",
            "RANDOM EVENT: Music allowed in office! Productivity increased."
        ]

        if event_roll <= 15:
            print(random.choice(bad_texts))
            speed_modifier = 0.5
        elif event_roll >= 85:
            print(random.choice(good_texts))
            speed_modifier = 2.0
        else:
            speed_modifier = 1.0

        for emp in employees:
            emp.speed = speed_modifier
