phone_book_test1 = ["119", "97674223", "1195524421"]
phone_book_test2 = ["123", "456", "789"]
phone_book_test3 = ["12", "123", "1235", "567", "88"]


def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True


print(solution(phone_book_test1))  # false
print(solution(phone_book_test2))  # true
print(solution(phone_book_test3))  # false
