from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMessage

        fields = [
            "name",
            "email",
            "phone",
            "subject",
            "message",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class": (
                        "w-full rounded-lg border border-slate-300 "
                        "bg-white px-4 py-3 text-slate-900 "
                        "placeholder-slate-400 shadow-sm "
                        "outline-none transition "
                        "focus:border-blue-500 focus:ring-2 "
                        "focus:ring-blue-500/20"
                    ),
                    "placeholder": "Your name",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": (
                        "w-full rounded-lg border border-slate-300 "
                        "bg-white px-4 py-3 text-slate-900 "
                        "placeholder-slate-400 shadow-sm "
                        "outline-none transition "
                        "focus:border-blue-500 focus:ring-2 "
                        "focus:ring-blue-500/20"
                    ),
                    "placeholder": "you@example.com",
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "class": (
                        "w-full rounded-lg border border-slate-300 "
                        "bg-white px-4 py-3 text-slate-900 "
                        "placeholder-slate-400 shadow-sm "
                        "outline-none transition "
                        "focus:border-blue-500 focus:ring-2 "
                        "focus:ring-blue-500/20"
                    ),
                    "placeholder": "+263 77 123 4567",
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "class": (
                        "w-full rounded-lg border border-slate-300 "
                        "bg-white px-4 py-3 text-slate-900 "
                        "placeholder-slate-400 shadow-sm "
                        "outline-none transition "
                        "focus:border-blue-500 focus:ring-2 "
                        "focus:ring-blue-500/20"
                    ),
                    "placeholder": "How can we help?",
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "class": (
                        "w-full min-h-[160px] resize-y rounded-lg "
                        "border border-slate-300 bg-white px-4 py-3 "
                        "text-slate-900 placeholder-slate-400 "
                        "shadow-sm outline-none transition "
                        "focus:border-blue-500 focus:ring-2 "
                        "focus:ring-blue-500/20"
                    ),
                    "placeholder": "Tell us about your project...",
                    "rows": 6,
                }
            ),
        }