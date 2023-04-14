from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in ["MainService", "SecondaryService"]:
            raise Exception("Invalid service type!")

        service = None

        if service_type == "MainService":
            service = MainService(name)
        elif service_type == "SecondaryService":
            service = SecondaryService(name)

        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in ["MaleRobot", "FemaleRobot"]:
            raise Exception("Invalid robot type!")

        robot = None

        if robot_type == "MaleRobot":
            robot = MaleRobot(name, kind, price)
        elif robot_type == "FemaleRobot":
            robot = FemaleRobot(name, kind, price)

        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next(filter(lambda r: r.name == robot_name, self.robots))
        service = next(filter(lambda s: s.name == service_name, self.services))

        if robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ == "SecondaryService":
            return "Unsuitable service."

        if robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ == "MainService":
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))

        try:
            robot = next(filter(lambda r: r.name == robot_name, service.robots))

            if robot:
                service.robots.remove(robot)
                self.robots.append(robot)

                return f"Successfully removed {robot_name} from {service_name}."

        except StopIteration:
            raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))

        total_price = 0

        for robot in service.robots:
            total_price += robot.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []

        for service in self.services:
            result.append(f"{service.details()}\n")

        return ''.join(result)[:-1]
