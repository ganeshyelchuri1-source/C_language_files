struct Node* reverseList(struct Node* head) {
    struct Node *prev = NULL, *current = head, *next = NULL;
    while (current != NULL) {
        next = current->next;  // 1. Store next node
        current->next = prev;  // 2. Reverse current node's pointer
        prev = current;        // 3. Move pointers forward
        current = next;
    }
    return prev; // New head
}