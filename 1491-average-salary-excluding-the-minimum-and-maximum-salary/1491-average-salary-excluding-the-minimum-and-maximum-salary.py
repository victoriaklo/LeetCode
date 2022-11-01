class Solution:
    def average(self, salary: List[int]) -> float:
        sorted_salary = (sorted(salary))
        total = sum(sorted_salary[1:-1])
        return total/(len(salary)-2)