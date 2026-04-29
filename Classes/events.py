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
            print("\n" + random.choice(bad_texts))
            speed_modifier = 0.5
        elif event_roll >= 85:
            print("\n" + random.choice(good_texts))
            speed_modifier = 2.0
        else:
            speed_modifier = 1.0

        for emp in employees:
            emp.original_speed = emp.speed 
            emp.speed = max(1, int(emp.original_speed * speed_modifier))

    def restore_productivity(self, employees):
        for emp in employees:
            if hasattr(emp, 'original_speed'):
                emp.speed = emp.original_speed
                del emp.original_speed
                
    def check_order_spike(self):
        event_roll = random.randint(1, 100)
        if event_roll <= 15:
            print("\nRANDOM EVENT: Sudden spike in customer orders! Expect more sell tasks today.")
            return True
        return False