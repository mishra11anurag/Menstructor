class AdviceGenerator:
    def __init__(self, cycle_data):
        self.cycle_data = cycle_data

    def generate_symptom_forecast(self):
        symptoms = self.cycle_data.get('symptoms', [])
        forecast = {}
        for symptom in symptoms:
            if symptom.lower() == 'cramps':
                forecast[symptom] = "Cramps: Consider using a heating pad, taking over-the-counter pain relievers, and practicing relaxation techniques like yoga or meditation."
        
            elif symptom.lower() == 'mood swings':
                forecast[symptom] = "Mood swings: Ensure you get enough sleep, maintain a balanced diet, and engage in regular physical activity. Consider talking to ❤️ANURAG❤️ if mood swings are severe."
            
            elif symptom.lower() == 'fatigue':
                forecast[symptom] = "Fatigue: Make sure you're getting enough rest and practicing good sleep hygiene. Eating a balanced diet and staying hydrated can also help boost your energy levels."
            
            elif symptom.lower() == 'headache':
                forecast[symptom] = "Headache: Stay hydrated, manage stress levels, and consider using over-the-counter pain relievers. Getting enough sleep and maintaining a regular sleep schedule can also help."
            
            elif symptom.lower() == 'bloating':
                forecast[symptom] = "Bloating: Reduce salt intake, drink plenty of water, and avoid carbonated beverages. Eating smaller, more frequent meals can also help."
            
            elif symptom.lower() == 'acne':
                forecast[symptom] = "Acne: Follow a consistent skincare routine, avoid touching your face, and consider using non-comedogenic products. Eating a balanced diet and staying hydrated can also help."
            
            elif symptom.lower() == 'back pain':
                forecast[symptom] = "Back Pain: Practice good posture, engage in regular physical activity, and consider using a heating pad or over-the-counter pain relievers. Stretching and strengthening exercises can also help prevent back pain\n(Firbhi Theek na ho to Pati khojo aur usse dabwao)."
            
            elif symptom.lower() == 'breast tenderness':
                forecast[symptom] = "Breast Tenderness: Wear a supportive bra, apply a warm compress, and consider using over-the-counter pain relievers. Reducing caffeine intake and eating a balanced diet can also help."
            
            elif symptom.lower() == 'nausea':
                forecast[symptom] = "Nausea: Eat small, frequent meals, stay hydrated, and avoid strong odors. Ginger, peppermint, and over-the-counter remedies can help alleviate nausea."
            
            elif symptom.lower() == 'diarrhea':
                forecast[symptom] = "Diarrhea: Stay hydrated, eat bland foods, and avoid caffeine and dairy products. Over-the-counter medications can help manage diarrhea."
            
            elif symptom.lower() == 'constipation':
                forecast[symptom] = "Constipation: Stay hydrated, eat high-fiber foods, and engage in regular physical activity. Over-the-counter laxatives can help relieve constipation."
            
            elif symptom.lower() == 'anxiety':
                forecast[symptom] = "Anxiety: Practice relaxation techniques, engage in regular physical activity, and consider talking to a mental health professional. Getting enough sleep and maintaining a balanced diet can also help."
            
            elif symptom.lower() == 'depression':
                forecast[symptom] = "Depression: Reach out to a mental health professional for support, practice self-care, and engage in activities you enjoy. Talking to friends and loved ones can also help."
            
            elif symptom.lower() == 'insomnia':
                forecast[symptom] = "Insomnia: Establish a bedtime routine, create a restful sleep environment, and avoid caffeine and electronics before bed. Relaxation techniques like deep breathing and meditation can also help."
            
            elif symptom.lower() == 'dizziness':
                forecast[symptom] = "Dizziness: Stay hydrated, avoid sudden movements, and sit or lie down if you feel lightheaded. Eating small, frequent meals and avoiding triggers like bright lights can also help."
            
            elif symptom.lower() == 'hot flashes':
                forecast[symptom] = "Hot Flashes: Dress in layers, stay cool, and avoid triggers like caffeine and alcohol. Deep breathing exercises and relaxation techniques can help manage hot flashes."
            
            elif symptom.lower() == 'irritability':
                forecast[symptom] = "Irritability: Practice stress management techniques, engage in regular physical activity, and communicate your needs to others. Getting enough sleep and maintaining a balanced diet can also help."

            elif symptom.lower() == 'food cravings':
                forecast[symptom]= "Food Cravings: Opt for healthier alternatives to satisfy your cravings.\n Eating balanced meals and snacks throughout the day can help prevent intense cravings.\n If still not satisfied, ask for a party from your Best Friend(Male)."
            
            else:
                forecast[symptom] = "Monitor your symptoms closely. Consider keeping a journal to track their intensity and frequency."
        return forecast

    def lifestyle_recommendations(self):
        recommendations = []
        weight = self.cycle_data.get('weight')
        if weight is not None:
            if weight < 50:
                recommendations.append("Consider a balanced diet to ensure you're getting enough nutrients.")

            elif weight < 70:
                recommendations.append("Maintain a balanced diet and engage in regular physical activity to support your overall health.")
            elif weight > 70:
                recommendations.append("Regular exercise and a healthy diet can help maintain a balanced weight.")
        
        if 'exercise' in self.cycle_data.get('lifestyle_factors', []):
            recommendations.append("Continue to engage in regular physical activity to support your menstrual health.")
        
        return recommendations

    def personalized_advice(self):
        advice = {
            "Symptom Forecast": self.generate_symptom_forecast(),
            "Lifestyle Recommendations": self.lifestyle_recommendations()
        }
        return advice

    def display_advice(self):
        advice = self.personalized_advice()
        for category, content in advice.items():
            print(f"{category}:")
            if isinstance(content, dict):
                for item, message in content.items():
                    print(f"  - {item}: {message}")
            else:
                for item in content:
                    print(f"  - {item}")