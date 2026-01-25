import unittest
from LAB1 import Solution

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_basic_case(self):
        nums = [2, 7, 11, 15]
        target = 9
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), [0, 1])
        self.assertEqual(nums[result[0]] + nums[result[1]], target)
    
    def test_negative_numbers(self):
        nums = [-3, 4, 3, 90]
        target = 0
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), [0, 2])
        self.assertEqual(nums[result[0]] + nums[result[1]], target)
    
    def test_duplicate_numbers(self):
        nums = [3, 3]
        target = 6
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), [0, 1])
        self.assertEqual(nums[result[0]] + nums[result[1]], target)
    
    def test_large_numbers(self):
        nums = [1000000, 500000, 1500000]
        target = 2000000
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), [1, 2])  
        self.assertEqual(nums[result[0]] + nums[result[1]], target)
    
    def test_no_solution(self):
        nums = [1, 2, 3, 4]
        target = 10
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [])
    
    def test_zero_target(self):
        nums = [0, 4, 3, 0]
        target = 0
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), [0, 3])
        self.assertEqual(nums[result[0]] + nums[result[1]], target)
    
    def test_single_element(self):
        nums = [5]
        target = 5
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [])
    
    def test_three_elements(self):
        nums = [1, 2, 3]
        target = 5
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), [1, 2])
        self.assertEqual(nums[result[0]] + nums[result[1]], target)



if __name__ == "__main__":
    unittest.main(verbosity=2)
