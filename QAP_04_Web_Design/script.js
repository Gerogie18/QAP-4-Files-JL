const motel_customer = {
    customerID: 1001,
    name: "Ashley Traverse",
    birthdate: "1990-05-15",
    gender: "X",
    roomPreferences: ["Single Room", "East-facing Room"],
    address: {
        street: "21 Main St",
        city: "Grand Falls Windsor",
        province: "NL",
        postal_code: "A0A 3H3"
    },
    previousBookingID: [2021120822, 2019080713],
    currentBookingID: 2024072102,
    checkinDate: "2024-07-21",
    checkoutDate: "2024-07-28",
    roomType: "Standard Room",
    roomNumber: "101",
    roomRate: 200,
    paymentMethod: "Credit Card",
    notes: ["Foreward Calls for Howard Murphey"],

    // Method to calculate age
    calculateAge: function() {
        const birthdate = new Date(this.birthdate);
        const currentDate = new Date();
        let age = currentDate.getFullYear() - birthdate.getFullYear();
        const monthDiff = currentDate.getMonth() - birthdate.getMonth();
        if (monthDiff < 0 || (monthDiff === 0 && currentDate.getDate() < birthdate.getDate())) {
            age--;
        }
        return age;
    },

    // Method to calculate duration of stay
    calculateDurationOfStay: function() {
        const checkinDate = new Date(this.checkinDate);
        const checkoutDate = new Date(this.checkoutDate);
        const duration = Math.abs(checkoutDate - checkinDate) / (1000 * 60 * 60 * 24);
        return duration;
    }
};

document.addEventListener("DOMContentLoaded", () => {
    document.write(`
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sunset Motel - Customer Info</title>
        <link rel="stylesheet" href="styles.css"> 

        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Vast+Shadow&display=swap" rel="stylesheet">

    </head>
    <body>
        <aside><img src="images/background.jpg" width="95%" height="100%"></aside>
        <div class="maincontent">
            <div class="info">
                <h1>Sunset Motel - Customer Data</h1>
                <h2>Customer ${motel_customer.customerID}</h2>
                <p>Name: ${motel_customer.name}<br>
                Birthdate: ${motel_customer.birthdate}<br>
                Age: ${motel_customer.calculateAge()}<br>
                Gender: ${motel_customer.gender}<br>
                Address: ${motel_customer.address.street}, ${motel_customer.address.city}, ${motel_customer.address.province}, ${motel_customer.address.postal_code}<br>
                Booking ID: ${motel_customer.currentBookingID}<br>
                Duration of Stay: ${motel_customer.calculateDurationOfStay()} days<br>
                Checkedin: ${motel_customer.checkinDate}<br>
                Expected Checkout: ${motel_customer.checkoutDate}<br>
                <br></p>
                <h3> Room Preferences</h3>
                <ul>
                    ${motel_customer.roomPreferences.map(pref => `<li>${pref}</li>`).join('')}
                </ul>
                <br>
                <h3> Customer Notes: </h3>
                <ul>
                    ${motel_customer.notes.map(note => `<li>${note}</li>`).join('')}
                </ul>
            </div>
        </div>
    </body>
    `);
});
