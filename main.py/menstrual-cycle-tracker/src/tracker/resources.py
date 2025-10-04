class ResourceProvider:
    def __init__(self):
        self.resources = {
            "articles": [
                {
                    "title": "Understanding Your Menstrual Cycle",
                    "link": "https://www.example.com/understanding-menstrual-cycle"
                },
                {
                    "title": "Tips for Tracking Your Cycle",
                    "link": "https://www.example.com/tips-for-tracking-cycle"
                }
            ],
            "support_materials": [
                {
                    "title": "Menstrual Health FAQs",
                    "link": "https://www.example.com/menstrual-health-faqs"
                },
                {
                    "title": "Healthy Lifestyle Tips",
                    "link": "https://www.example.com/healthy-lifestyle-tips"
                }
            ],
            "external_links": [
                {
                    "title": "Planned Parenthood",
                    "link": "https://www.plannedparenthood.org"
                },
                {
                    "title": "The American College of Obstetricians and Gynecologists",
                    "link": "https://www.acog.org"
                }
            ]
        }

    def get_resources(self):
        return self.resources

    def display_resources(self):
        print("Educational Resources:")
        for category, items in self.resources.items():
            print(f"\n{category.replace('_', ' ').title()}:")
            for item in items:
                print(f"- {item['title']}: {item['link']}")