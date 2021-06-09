# 学習レポート

## LogisticRegression

```txt
=== CLASSIFICATION REPORT ===
model : LogisticRegression-count
Training Accuracy : 0.9792138213498004
Testing Accuracy : 0.9641164362494973

               precision    recall  f1-score   support

         Bad       0.96      0.87      0.92     28491
        Good       0.96      0.99      0.98     98308

    accuracy                           0.96    126799
   macro avg       0.96      0.93      0.95    126799
weighted avg       0.96      0.96      0.96    126799
```

## LinearSVC

* CountVectorizer

```txt
=== CLASSIFICATION REPORT ===
model : LinearSVC-count
Training Accuracy : 0.9988433136959545
Testing Accuracy : 0.9715691764130632

               precision    recall  f1-score   support

         Bad       0.96      0.91      0.94     28729
        Good       0.97      0.99      0.98     98070

    accuracy                           0.97    126799
   macro avg       0.97      0.95      0.96    126799
weighted avg       0.97      0.97      0.97    126799
```

* TfidfVectorizer

```txt
=== CLASSIFICATION REPORT ===
model : LinearSVC-tfidf
Training Accuracy : 0.9981098694258893
Testing Accuracy : 0.9732805463765487

               precision    recall  f1-score   support

         Bad       0.97      0.91      0.94     28521
        Good       0.97      0.99      0.98     98278

    accuracy                           0.97    126799
   macro avg       0.97      0.95      0.96    126799
weighted avg       0.97      0.97      0.97    126799
```
