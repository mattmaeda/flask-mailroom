"""
Entry point for the flask mailroom application
"""
import os

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    """ Main page for mailroom page.  Redirects to /donations """
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    """ Displays all donation records """
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/donations/<donor>')
def get_donation_by_donor(donor):
    """ Displays all donation records by donor name

    :param donor String: the donor name case-sensitive

    :return: donations by donor.  If donor does not exists, empty page is
             displayed
    """
    donations = Donation.select().join(Donor).where(Donor.name == donor)
    return render_template('donations.jinja2', donations=donations)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
