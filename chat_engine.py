import random

faq_db = {
    "simulation coordination": "Simulations are scheduled with the OLPD team and follow the Foundations training calendar.",
    "actor scheduling": "Actor hours are tracked for billing and coordinated via the vendor’s calendar.",
    "training materials": "All trainers must receive materials one week in advance, including binders and updated manuals.",
    "equipment support": "For tech issues, the Simulation Technician maintains camera, audio, smartboards, and streaming tools.",
    "qualifications": "This role requires a Bachelor's degree and 2 years in human services or education coordination. Video/audio experience is a plus.",
    "video review": "Simulation videos will be stored in the DCFS-approved storage and accessible by supervisors and trainees."
}

def get_response(query):
    for key, value in faq_db.items():
        if key in query.lower():
            return value
    return random.choice([
        "Let me look into that for you…",
        "I'm still learning that area. Try asking about simulation, training, or actors.",
        "That might require manual lookup—check with the Foundations team or OLPD calendar."
    ])