"use client"
import { useState, React, useEffect } from 'react'
import './styles.css'
import Link from 'next/link';

import logo from '@/assets/logo.png';

export default function Navbar() {

  const [menuOpen, setMenuOpen] = useState(null)

  useEffect(() => {
    function handleClickOutside(event) {
      if (menuOpen && !event.target.closest('.menu-wrapper'))
        setMenuOpen(false);
    }

    document.addEventListener('click', handleClickOutside);

    return () => {
        document.removeEventListener('click', handleClickOutside);
    };
  }, [menuOpen]);

  return (
    <header>
      <nav 
        className="navbar" 
        style={{ backgroundColor: menuOpen ? 'var(--bg-light-strong)' : 'var(--header-transparent)' }}>
        <Link href='/#about' className='logo'>
          <img src={logo.src} alt="Logo do site: texto 'futura dev' envolvido por símbolos digitais" />
        </Link>

        <div className='menu-wrapper'>
          <div
            className={`hamburguer ${menuOpen !== null && (menuOpen ? 'close' : 'open')}`}
            role='button'
            onClick={() => setMenuOpen(!menuOpen)}
          >
            <span />
            <span />
          </div>

          <ul
            className={menuOpen !== null ? (menuOpen ? 'opened' : 'closed') : undefined}
            onClick={() => menuOpen && setMenuOpen(false)}
          >   
            <li>
              <Link href="/#about">Início</Link >
            </li>
            <li>
              <Link href="/quiz">Enquetes</Link >
            </li>
            <li>
              <Link href="/#cause">Nossa causa</Link >
            </li>
          </ul>
        </div>
      </nav>

      {menuOpen && <div className='fade fade-menu show' />}
    </header>
  )
}