from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields here

class Lesson(models.Model):
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title
    
    def get_flashcards(self):
        return FlashCard.objects.filter(lesson=self)

class PartOfSpeech:
    NOUN = 'N'
    VERB = 'V'
    ADJECTIVE = 'Adj'
    ADVERB = 'Adv'
    CONJUNCTION = 'Con'
    PHRASAL_VERB = 'PhV'
    OTHER = 'O'
    # Add more parts of speech as needed

    CHOICES = [
        (NOUN, 'Noun'),
        (VERB, 'Verb'),
        (ADJECTIVE, 'Adjective'),
        (ADVERB, 'Adverb'),
        (CONJUNCTION, 'Conjunction'),
        (PHRASAL_VERB, 'Phrasal Verb'),
        (OTHER, 'Other'),
        # Add more choices here
    ]

class FlashCard(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=400)
    answer_text = models.CharField(max_length=400)
    part_of_speech = models.CharField(max_length=10, choices=PartOfSpeech.CHOICES, blank=True)

    def __str__(self):
        return self.question_text
    
    def get_hint(self):
        return Hint.objects.filter(flashCard=self)

class Hint(models.Model):
    flashCard = models.OneToOneField(FlashCard, on_delete=models.CASCADE)
    synonyms = models.JSONField(null=True, blank=True)  # Store a list of strings as JSON
    usage_example = models.CharField(max_length=400, null=True, blank=True)
    note = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        parts = []
        
        if self.synonyms:
            parts.append(f"Synonyms: {', '.join(self.synonyms)}")
        
        if self.usage_example:
            parts.append(f"Usage: {self.usage_example}")
        
        if self.note:
            parts.append(f"Note: {self.note}")
        
        if not parts:
            return "Hint is empty"
        
        return ', '.join(parts)

