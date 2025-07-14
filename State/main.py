
# Step 1: Define the State Interface

from abc import ABC, abstractmethod

class DocumentState(ABC):
    @abstractmethod
    def submit(self, document):
        pass

    @abstractmethod
    def approve(self, document):
        pass

    @abstractmethod
    def reject(self, document):
        pass

# Step 2: Create Concrete State Classes

class DraftState(DocumentState):
    def submit(self, document):
        print("Submitting the document.")
        document.state = SubmittedState()

    def approve(self, document):
        print("Cannot approve a document in Draft state.")

    def reject(self, document):
        print("Cannot reject a document in Draft state.")


class SubmittedState(DocumentState):
    def submit(self, document):
        print("Document is already submitted.")

    def approve(self, document):
        print("Approving the document.")
        document.state = ApprovedState()

    def reject(self, document):
        print("Rejecting the document.")
        document.state = RejectedState()


class ApprovedState(DocumentState):
    def submit(self, document):
        print("Document is already approved and cannot be submitted again.")

    def approve(self, document):
        print("Document is already approved.")

    def reject(self, document):
        print("Cannot reject an approved document.")


class RejectedState(DocumentState):
    def submit(self, document):
        print("Cannot submit a rejected document.")

    def approve(self, document):
        print("Cannot approve a rejected document.")

    def reject(self, document):
        print("Document is already rejected.")


# Step 3: Create the Context Class (Document)


class Document:
    def __init__(self):
        self.state = DraftState()  # Initial state is Draft

    def submit(self):
        self.state.submit(self)

    def approve(self):
        self.state.approve(self)

    def reject(self):
        self.state.reject(self)

# Usage

# Create a document and perform state transitions
doc = Document()

# Document in Draft state
doc.submit()   # Submitting the document
doc.approve()  # Approving the document

# Document is now in Approved state
doc.reject()   # Attempting to reject an approved document (should be invalid)
