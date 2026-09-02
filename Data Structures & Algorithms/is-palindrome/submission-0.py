class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = "".join(char for char in s if char.isalnum())
        clean_text = clean_text.lower()
        start = 0
        back = len(clean_text) - 1
        while start <= back:
            if start == back:
                return True
            elif clean_text[start] == clean_text[back]:
                start += 1
                back -= 1
            else:
                return False
        return True

        