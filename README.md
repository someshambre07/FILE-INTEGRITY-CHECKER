# FILE-INTEGRITY-CHECKER

**COMPANY**:CODTECH IT SOLUTIONS

**NAME**:SOMESH SANTOSH AMBRE

**INTERN ID**:CT08HYJ

**DOMAIN**:CYBER SECURITY AND ETHICAL HACKING

**BATCH DURATION**:JANUARY 10TH,2025 TO FEBRUARY 10TH,2025

**MENTOR NAME**:NEELA SANTHOSH KUMAR

#PROJECT DESCRIPTION:-
In today's digital age, ensuring the integrity of files is critical for maintaining data security and detecting unauthorized modifications. As part of my internship at CodTech, I have developed a Python-based File Integrity Checker, a powerful tool designed to monitor changes in files by calculating and comparing their hash values. This tool plays a vital role in safeguarding sensitive data, preventing tampering, and maintaining system reliability.

Objective
The primary objective of this project is to create a Python script that can efficiently verify the integrity of files. By leveraging libraries like hashlib, the tool calculates cryptographic hash values for files and compares them to detect any changes, whether due to corruption, tampering, or unauthorized access. The deliverable is a fully functional script that provides users with an intuitive and reliable mechanism for monitoring file integrity.

Implementation
The File Integrity Checker is built using Python and its standard library, particularly hashlib. The implementation includes the following core functionalities:

Hash Value Calculation:
The tool generates unique cryptographic hash values (e.g., MD5, SHA-256) for each monitored file. These hashes act as digital fingerprints, ensuring that even the slightest file alteration results in a different hash value.

Initial Baseline Creation:
During the first execution, the tool computes hash values for all target files and stores them securely in a reference database or a text file. This baseline serves as a reference for future integrity checks.

File Monitoring:
The tool periodically re-scans the files, recalculates their hash values, and compares them with the stored baseline. If discrepancies are detected, the tool flags the files as modified.

Change Reporting:
A detailed log report is generated, highlighting which files have been altered, added, or deleted. This ensures users have clear visibility of any file-related activities.


Benefits
The File Integrity Checker provides several benefits:

Enhanced Security: It detects unauthorized changes in files, preventing potential cyber threats or data breaches.
Reliability: Ensures that critical files remain unaltered, maintaining the integrity of applications and systems.
Ease of Use: With a simple Python script, the tool is lightweight, portable, and easily deployable across various systems.
Challenges and Solutions

Conclusion
This File Integrity Checker is a significant contribution to the field of cybersecurity, enabling organizations to maintain file authenticity and detect malicious activity effectively. By leveraging the power of Python and cryptographic techniques, the project underscores the importance of file integrity in securing digital assets.


