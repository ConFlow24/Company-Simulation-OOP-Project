import random


class Event:
    """
    This class handles random events that can affect employee productivity and attendance.
    The group added this to represent real life scenarios where unexpected events can impact the workplace.

    """

    def random_productivity(self, employees):
        """
        This function randomly produces an event (bad or good) for each day.

        Bad and Good events can have a 15% chance to occur and will decrease or increase employee productivity (- 0.5x or + 2x speed).
        70% chance for no event to occur, keeping productivity normal.

        Args:
            employees (list): List of Employee objects whose productivity will be affected by the random event.
        """

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
            speed_modifier = 0.5  # for bad events, employee speed - 0.5x
        elif event_roll >= 85:
            print("\n" + random.choice(good_texts))
            speed_modifier = 2.0  # for good events, employee speed + 2x
        else:
            speed_modifier = 1.0  # no event, so normal speed

        for emp in employees:
            emp.original_speed = emp.speed  # saves the original speed before modifying
            emp.speed = max(1, int(emp.original_speed * speed_modifier))

    def restore_productivity(self, employees):
        """
        This function restores employee productivity to their original speed.

        Args:
            employees (list): List of Employee objects whose productivity will be restored.
        """
        for emp in employees:
            # hasattr means "has attribute". Checks if the employee has the original_speed attribute before trying to restore it.
            if hasattr(emp, 'original_speed'):
                emp.speed = emp.original_speed
                del emp.original_speed

    def check_order_spike(self):
        """
        This function randomly checks for a sudden spike in customer orders for each day.

        There is a 15% chance for it to happen, which multiplies the number of sell tasks generated
        for the day by 4.

        It return True if there is a spike, andFalse if there is not.
        """

        event_roll = random.randint(1, 100)
        if event_roll <= 15:
            print(
                "\nRANDOM EVENT: Sudden spike in customer orders! Expect more sell tasks today.")
            return True
        return False
