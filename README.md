# project-team-53
USER MANUAL
Ομάδα 53
Ο χρήστης πρέπει μέσω του command prompt να τρέξει το αρχείο “start_game.py”.
(Προσοχή το πρόγραμμα δεν θα λειτουργήσει αν ο χρήστης τρέξει το πρόγραμμα κατευθείαν από το IDLE ή κάποιο άλλο πρόγραμμα επεξεργασίας κώδικα!)
Στο Linux και macos δεν χρειάζεται κάποια προετοιμασία αλλά στα Windows είναι απαραίτητο να εγκατασταθεί η βιβλιοθήκη curses μέσω pip install.
Εντός του menu η διαδικασία πλοήγησης γίνεται με τα βελάκια του πληκτρολογίου (πάνω και κάτω βέλος). 
Ο χρήστης επιλέγει μια από τις τρεις επιλογές που του δίνονται πατώντας Enter.
Ο χρήστης επιλέγοντας Play, ξεκινάει το παιχνίδι και στην συνέχεια έχει τον έλεγχο του φιδιού μέσω
από βελάκια όπου πρέπει να οδηγήσει το φίδι (που απεικονίζεται με το ‘0’) προς το φαγητό που
(απεικονίζεται με ‘@’) και έτσι να μεγαλώσει το μήκος του φιδιού κατά ένα ‘0’ και να συλλέξει ένα
πόντο. Σκοπός του παίκτη είναι να κάνει το φίδι όσο μεγαλύτερο μπορεί. Κατά τη διάρκεια του
παιχνιδιού υπάρχει δυνατότητα παύσης με το πλήκτρο “P”. Τέλος όταν ο χρήστης χάσει, είτε
πέφτοντας στον τοίχο είτε ακουμπώντας το κεφάλι φιδιού στο υπόλοιπο σώμα, θα του ζητηθεί να
πληκτρολογήσει το όνομα του (μέχρι 10 χαρακτήρες) και τέλος να πατήσει ‘ENTER’ ή ‘CTRL + G’ για
να ολοκληρωθεί η διαδικασία. Αν ο χρήστης δεν καταχωρήσει κανένα όνομα τότε το σκορ του καταχωρείται κάτω από το όνομα Annon(Από την λέξη anonymous).
(Προσοχή! Ο χρήστης μπορεί να δώσει μόνο αγγλικούς χαρακτήρες και αριθμούς). Έπειτα από αυτό
ο χρήστης επιστρέφει στο αρχικό μενού.
Ο χρήστης επιλέγοντας Scoreboard θα εμφανιστούν στην οθόνη τα σκορ τον προηγούμενων
παικτών(εφόσον υπάρχουν),με φθίνουσα σειρά, και πατώντας οποιοδήποτε πλήκτρο θα επιστρέψει
στο αρχικό μενού.
Σε αυτό το σημείο πρέπει να σημειωθεί ότι λόγω ενός bug ο χρήστης, όταν παίξει και επιστρέψει στο
μενού το ‘scoreboard’ δεν θα ανταποκριθεί, έτσι ο χρήστης θα πρέπει να ξανατρέξει το παιχνίδι και
το scoreboard λειτουργεί κανονικά.
Ο χρήστης επιλέγοντας Exit τερματίζει την εφαρμογή
