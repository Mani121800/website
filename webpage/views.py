from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import EmailMessage


# def home(request):
#     return render(request, 'home.html')

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def pricing(request):
    return render(request,"pricing.html")

def blog(request):
    return render(request,"blog.html")

def contact(request):
    return render(request,"contact.html")


def home(request):
    context = {
        'title': 'Aura Harks Technology',
        'meta_description': 'Aura Harks Technology delivers cutting-edge IT services and solutions. From product development and web development to data analysis and AI & ML design, we empower your business with expert solutions.',
        'canonical_url': 'https://www.auraharkstechnology.com/',
        'og_title': 'Aura Harks Technology',
        'og_description': 'Aura Harks Technology provides advanced IT services and solutions including product development, web development, data analysis, and AI & ML design.',
        'og_url': 'https://www.auraharkstechnology.com/',
        'linkedin_title': 'Aura Harks Technology',
        'linkedin_description': 'Aura Harks Technology provides advanced IT services and solutions including product development, web development, data analysis, and AI & ML design.',
    }
    return render(request, 'home.html', context)




def send_message(request):
    success_message = None
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Define the email content
        subject = f"Message from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = 'poornasubash2718@gmail.com'

        # Send the email
        email = EmailMessage(subject, body, from_email, [to_email])
        email.send()

        success_message = "Thank you for your message! Will get back to you soon."

    return render(request, 'contact.html', {'success_message': success_message})



def plan_features(request):
    features = [
        "Web Application",
        "Ad Management",
        "Live Chat",
        "Multi-Language Content",
        "Conversational Bots",
        "Programmable Chatbots",
        "Basic SEO Setup",
        "1 Custom Landing Page",
        "Basic Social Media Integration",
        "Advanced SEO Optimization",
        "A/B Testing for Landing Pages",
        "Email Marketing Automation",
        "Custom Chatbot Flows",
        "Branding Kit",
        "Priority Support",
        "Custom Web Development",
        "Full Digital Marketing Strategy",
        "Premium SEO Package",
        "Full Chatbot Integration",
        "Lead Scoring & Automation",
        "Analytics&Conversion Optimization",
        "Dedicated Account Manager",
        "24/7 Priority Support",
        "Custom Web Application",
        "Advanced Ad Management",
        "Enterprise Live Chat",
        "Full Multi-Language Content",
        "Advanced Conversational Bots",
        "Fully Programmable Chatbots",
        "CRM & ERP Integration",
        "AI-Powered Personalization",
        "Custom Mobile App Development",
        "Cloud Hosting and Security",
        "Dedicated 24/7 Support & SLA",
        "Custom Analytics Dashboard",
        "VIP Onboarding & Training",
        "DataAnalytics & AI Insights",
        "Custom Integrations"
    ]

    plan_features = {
        'Basic': [
            True, True, True, True, True, True, True, True, True,
            False, False, False, False, False, False,
            False, False, False, False, False, False,
            False, False, False, False, False, False,
            False, False, False, False, False, False,
            False, False, False, False, False
        ],
        'Silver': [
            True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True,
            False, False, False, False, False, False,
            False, False, False, False, False, False,
            False, False, False, False, False, False,
            False, False, False, False, False
        ],
        'Gold': [
            True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True,
            True, True, True, True, True, True,
            True, True, False, False, False, False,
            False, False, False, False, False, False,
            False, False, False, False, False
        ],
        'Platinum': [
            True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True,
            True, True, True, True, True, True,
            True, True, True, True, True, True,
            True, True, True, True, True, True,
            True, True, True, True, True
        ]
    }


    feature_availability = []
    for feature, basic, silver, gold, platinum in zip(features, *plan_features.values()):
        feature_availability.append({
            'feature': feature,
            'basic': basic,
            'silver': silver,
            'gold': gold,
            'platinum': platinum
        })

    return render(request, 'plan_features1.html', {
        'feature_availability': feature_availability
    })






