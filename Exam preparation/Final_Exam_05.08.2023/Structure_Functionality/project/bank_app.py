from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENT_TYPES = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in BankApp.VALID_LOAN_TYPES:
            raise Exception("Invalid loan type!")

        loan = BankApp.VALID_LOAN_TYPES[loan_type]()
        self.loans.append(loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in BankApp.VALID_CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if self.capacity <= len(self.clients):  # marker
            return f"Not enough bank capacity."

        client = BankApp.VALID_CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = [l for l in self.loans if l.type == loan_type][0]
        client = [c for c in self.clients if c.client_id == client_id][0]

        if not (client.type == "Student" and loan.type == "StudentLoan") and \
            not (client.type == "Adult" and loan.type == "MortgageLoan"):  # marker
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = [c for c in self.clients if c.client_id == client_id]
        if not client:
            raise Exception("No such client!")

        client = client[0]

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)

        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        loans_of_given_type = [l for l in self.loans if l.type == loan_type]

        number_of_changed_loans = 0

        for l in loans_of_given_type:
            l.increase_interest_rate()
            number_of_changed_loans += 1

        return f"Successfully changed {number_of_changed_loans} loans."  # len(loans_of_given_type)

    def increase_clients_interest(self, min_rate: float):
        clients = [c for c in self.clients if c.interest < min_rate]

        [c.increase_clients_interest() for c in clients]

        return f"Number of clients affected: {len(clients)}."

    def get_statistics(self):
        total_clients_income = 0
        loans_count_granted_to_clients = 0
        granted_sum = 0
        not_granted_sum = sum([l.amount for l in self.loans])
        sum_clients_interest_rate = 0
        avg_client_interest_rate = 0

        for c in self.clients:
            total_clients_income += c.income
            loans_count_granted_to_clients += len(c.loans)
            granted_sum += sum([l.amount for l in c.loans])
            sum_clients_interest_rate += c.interest

        if self.clients:
            avg_client_interest_rate = sum_clients_interest_rate / len(self.clients)

        return (f"Active Clients: {len(self.clients)}\n"
                f"Total Income: {total_clients_income:.2f}\n"
                f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"
                f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n"
                f"Average Client Interest Rate: {avg_client_interest_rate:.2f}")

