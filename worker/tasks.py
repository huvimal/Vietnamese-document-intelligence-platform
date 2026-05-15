from celery import Celery

celery = Celery(
    "worker",
    broker="redis://redis:6379/0"
)

@celery.task
def process_document(document_path):

    print(f"Processing: {document_path}")

    return {
        "status": "completed"
    }