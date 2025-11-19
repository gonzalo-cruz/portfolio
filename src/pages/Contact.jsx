import React, { useState } from 'react';

const Contact = () => {
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isSuccess, setIsSuccess] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevents the page from reloading
    setIsSubmitting(true);

    const formData = new FormData(e.target);

    try {
      // REPLACE WITH YOUR ACTUAL FORMSPREE LINK
      const response = await fetch("https://formspree.io/f/mblwkdzq", {
        method: "POST",
        body: formData,
        headers: {
          'Accept': 'application/json'
        }
      });

      if (response.ok) {
        setIsSuccess(true); // Shows the success message
        e.target.reset();   // Clears the form
      } else {
        alert("Oops! There was a problem submitting your form");
      }
    } catch (error) {
      alert("Error submitting form");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="min-h-screen bg-paper dark:bg-warm-black px-6 py-12 md:py-20 transition-colors duration-500">
      <div className="max-w-xl mx-auto">
        
        {/* SUCCESS MESSAGE SECTION */}
        {isSuccess ? (
          <div className="bg-parchment dark:bg-warm-surface border border-rust/50 rounded-xl p-8 text-center shadow-lg animate-fade-in">
            <div className="w-16 h-16 bg-rust text-white rounded-full flex items-center justify-center mx-auto mb-4 text-3xl">
              ✓
            </div>
            <h2 className="text-2xl font-serif font-bold text-ink dark:text-warm-text mb-2">Message Sent!</h2>
            <p className="text-ink-light dark:text-warm-subtext mb-6">
              Thanks for reaching out, I'll get back to you soon.
            </p>
            <button 
              onClick={() => setIsSuccess(false)}
              className="text-rust font-medium hover:underline"
            >
              Send another message
            </button>
          </div>
        ) : (
          // FORM SECTION
          <>
            <h1 className="text-4xl font-serif font-bold text-ink dark:text-warm-text mb-4">Get in Touch</h1>
            <p className="text-ink-light dark:text-warm-subtext mb-12">
              Have a question or want to work together? Drop me a message below.
            </p>

            <form onSubmit={handleSubmit} className="flex flex-col gap-6">
              
              <div>
                <label htmlFor="name" className="block text-sm font-medium text-ink dark:text-warm-text mb-2">Name</label>
                <input
                  id="name"
                  type="text" 
                  name="name"
                  required
                  className="w-full p-3 rounded-lg bg-parchment dark:bg-warm-surface border border-paper-border dark:border-warm-border text-ink dark:text-warm-text focus:outline-none focus:ring-2 focus:ring-rust/50 transition-all"
                  placeholder="Your Name"
                />
              </div>

              <div>
                <label htmlFor="email" className="block text-sm font-medium text-ink dark:text-warm-text mb-2">Email</label>
                <input
                  id="email"
                  type="email" 
                  name="email"
                  required
                  className="w-full p-3 rounded-lg bg-parchment dark:bg-warm-surface border border-paper-border dark:border-warm-border text-ink dark:text-warm-text focus:outline-none focus:ring-2 focus:ring-rust/50 transition-all"
                  placeholder="your@email.com"
                />
              </div>

              <div>
                <label htmlFor="message" className="block text-sm font-medium text-ink dark:text-warm-text mb-2">Message</label>
                <textarea
                  id="message"
                  name="message"
                  rows="5"
                  required
                  className="w-full p-3 rounded-lg bg-parchment dark:bg-warm-surface border border-paper-border dark:border-warm-border text-ink dark:text-warm-text focus:outline-none focus:ring-2 focus:ring-rust/50 transition-all"
                  placeholder="How can I help you?"
                />
              </div>

              <button 
                type="submit" 
                disabled={isSubmitting}
                className="bg-rust text-white py-3 px-6 rounded-full font-medium hover:bg-ink hover:shadow-lg transform hover:-translate-y-1 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {isSubmitting ? 'Sending...' : 'Send Message'}
              </button>
            </form>
          </>
        )}
      </div>
    </div>
  );
};

export default Contact;