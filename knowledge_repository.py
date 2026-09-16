
knowledge_repository = {
    "Returns": {
        "Question": "How can a customer return a product?",
        "Answer": "The customer can request a return within 7 days of delivery."
    },

    "Refunds": {
        "Question": "When will the refund be processed?",
        "Answer": "Refunds are generally processed within 5-7 business days."
    },

    "Delivery": {
        "Question": "What should be done if an order is delayed?",
        "Answer": "The customer should check the tracking details or contact customer support."
    },

    "Damaged_Product": {
        "Question": "What should a customer do if the product is damaged?",
        "Answer": "The customer should upload product images and request a replacement or refund."
    },

    "Payment": {
        "Question": "What if payment is deducted but the order is not confirmed?",
        "Answer": "The amount is usually refunded automatically within a few working days."
    }
}


def display_knowledge_repository():
    print("E-COMMERCE CUSTOMER SUPPORT KNOWLEDGE REPOSITORY")
    print("------------------------------------------------")

    for category, information in knowledge_repository.items():
        print("\nCategory:", category)
        print("Question:", information["Question"])
        print("Answer:", information["Answer"])


def search_knowledge(query):
    query = query.lower()

    for category, information in knowledge_repository.items():
        if (query in category.lower()
                or query in information["Question"].lower()
                or query in information["Answer"].lower()):

            print("\nCategory:", category)
            print("Question:", information["Question"])
            print("Answer:", information["Answer"])
            return

    print("\nNo matching knowledge found.")


display_knowledge_repository()

print("\nSEARCH RESULT")
print("-------------")
search_knowledge("refund")