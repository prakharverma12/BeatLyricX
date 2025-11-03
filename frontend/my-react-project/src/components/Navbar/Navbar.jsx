import React from 'react';
import styles from './Navbar.module.css'; 
import logoImage from '../../assets/Logo.jpeg';
function Navbar() {
    // 2. Use the imported 'styles' object to apply classes
    return (
        <nav className={styles.navbar}>
            <a href="/" className={styles.logo}>
                <img src={logoImage} alt="Site Logo" />
            </a>

            <div className={styles.links}>
                <a href="/explore" className={styles.navLink}>Explore</a>
                <a href="/Leaderboard" className={styles.navLink}>Leaderboard</a>
                <a href="/Discuss" className={styles.navLink}>Discuss</a>
                <a href="/home" className={styles.navLink}>Home Page</a>
            </div>
        </nav>
    );
}

export default Navbar;