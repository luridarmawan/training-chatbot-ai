from transformers import pipeline
import time

customer_email = """
I am writing to pour my heart out about the recent unfortunate experience
I had with one of your coffee machines that arrived broken. I anxiously
unwrapped the box containing my highly anticipated coffee machine.
However, what I discovered within broke not only my spirit but also any
semblance of confidence I had placed in your brand.
Chapter 3 93
Its once elegant exterior was marred by the scars of travel, resembling a
war-torn soldier who had fought valiantly on the fields of some espresso
battlefield. This heartbreaking display of negligence shattered my dreams
of indulging in daily coffee perfection, leaving me emotionally distraught
and inconsolable
"""

start_time = time.time()

sentiment_model = pipeline(
    task="sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment"
)

print(sentiment_model(customer_email))

end_time = time.time()
execution_time = end_time - start_time

print(f"Waktu eksekusi: {execution_time} detik")