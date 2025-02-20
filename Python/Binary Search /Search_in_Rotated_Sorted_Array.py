def search(nums, target):
    # Initialize two pointers for the binary search
    left, right = 0, len(nums) - 1

    # Continue searching while the left pointer is less than or equal to the right pointer
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # Check if the middle element is the target
        if nums[mid] == target:
            return mid  # Return the index if found
        
        # Check which side of the array is sorted
        if nums[left] <= nums[mid]:  # Left side is sorted
            # Check if the target is in the sorted left side
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Narrow search to the left side
            else:
                left = mid + 1  # Target must be in the right side
        else:  # Right side is sorted
            # Check if the target is in the sorted right side
            if nums[mid] < target <= nums[right]:
                left = mid + 1  # Narrow search to the right side
            else:
                right = mid - 1  # Target must be in the left side

    return -1  # If we exit the loop, the target was not found

# Example usage
if __name__ == "__main__":
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    print(search(nums1, target1))  # Output: 4

    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3
    print(search(nums2, target2))  # Output: -1

    nums3 = [1]
    target3 = 0
    print(search(nums3, target3))  # Output: -1
