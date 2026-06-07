class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        chosen_array = matrix[0]

        while left <= right:
            midpoint_index = (right - left) // 2 + left
            mid_matrix = matrix[midpoint_index]

            if (
                mid_matrix[0] <= target
                and mid_matrix[len(mid_matrix) - 1] >= target
            ):
                chosen_array = mid_matrix
                break

            if mid_matrix[len(mid_matrix) - 1] < target:
                left = midpoint_index + 1
                chosen_array = mid_matrix

            elif mid_matrix[len(mid_matrix) - 1] > target:
                right = midpoint_index - 1
                chosen_array = mid_matrix

        # we have our found array now
        # for item in chosen_array:
        #     print(chosen_array)

        #     if item == target:
        #         return True
        l, r = 0, len(chosen_array) - 1
        while l <= r:
            midpoint = (r - l) // 2 + l

            if chosen_array[midpoint] == target:
                return True

            if chosen_array[midpoint] < target:
                l = midpoint + 1
            elif chosen_array[midpoint] > target:
                r = midpoint - 1



        return False