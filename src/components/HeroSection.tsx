import React from 'react';
import { motion } from 'framer-motion';

const HeroSection: React.FC = () => {
  return (
    <section className="relative min-h-[90vh] flex items-center justify-center overflow-hidden">
      {/* Floating background elements */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden">
        {/* Core floating particles - keeping the essential ones */}
        <div className="absolute top-1/4 left-1/4 w-4 h-4 bg-purple-400/30 rounded-full animate-float" style={{ animationDelay: '0s' }}></div>
        <div className="absolute top-1/3 right-1/3 w-3 h-3 bg-blue-400/40 rounded-full animate-float" style={{ animationDelay: '2s' }}></div>
        <div className="absolute bottom-1/4 left-1/3 w-5 h-5 bg-cyan-400/35 rounded-full animate-float" style={{ animationDelay: '4s' }}></div>
        <div className="absolute top-2/3 right-1/4 w-2 h-2 bg-purple-400/25 rounded-full animate-float" style={{ animationDelay: '6s' }}></div>
        <div className="absolute top-1/6 left-1/2 w-3 h-3 bg-blue-400/20 rounded-full animate-float" style={{ animationDelay: '1s' }}></div>
        <div className="absolute bottom-1/3 right-1/6 w-4 h-4 bg-cyan-400/30 rounded-full animate-float" style={{ animationDelay: '3s' }}></div>
        
        {/* A few gradient floating elements */}
        <div className="absolute top-1/4 right-1/6 w-6 h-6 bg-gradient-to-r from-purple-400/20 to-blue-400/20 rounded-full animate-float-slow" style={{ animationDelay: '1s' }}></div>
        <div className="absolute bottom-1/4 right-1/3 w-4 h-4 bg-gradient-to-r from-cyan-400/25 to-purple-400/25 rounded-full animate-float-slow" style={{ animationDelay: '3s' }}></div>
        
        {/* One glowing orb for subtle effect */}
        <div className="absolute top-1/6 right-1/4 w-8 h-8 bg-purple-400/10 rounded-full animate-pulse-glow blur-sm" style={{ animationDelay: '2s' }}></div>
      </div>
      
      <div className="relative z-10 text-center space-y-8 max-w-4xl mx-auto px-6">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="text-center space-y-6"
        >
          {/* Profile Picture */}
          <motion.div
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8, delay: 0.4 }}
            className="flex justify-center mb-8"
          >
            <div className="relative">
              <div className="w-32 h-32 md:w-40 md:h-40 rounded-full overflow-hidden border-4 border-white/20 shadow-2xl">
                <img
                  src="/1749219424811 (1).jpeg"
                  alt="Carlos Arroyo - Supply Chain & Analytics Professional"
                  className="w-full h-full object-cover"
                />
              </div>
              <div className="absolute inset-0 rounded-full bg-gradient-to-r from-blue-500/20 to-purple-500/20 animate-pulse"></div>
            </div>
          </motion.div>

          <h1 className="text-5xl md:text-7xl font-bold bg-gradient-to-r from-white to-gray-400 bg-clip-text text-transparent leading-tight">
            Carlos Arroyo
          </h1>
          <h2 className="text-2xl md:text-3xl font-semibold text-gray-300">
            Supply Chain & Analytics Professional
          </h2>
          <p className="text-lg md:text-xl text-gray-400 max-w-3xl mx-auto leading-relaxed">
            I optimize supply chain operations, implement intelligent systems, and leverage artificial intelligence 
            to transform logistics workflows. Building data-driven solutions that enhance operational efficiency 
            and drive strategic business decisions across global operations.
          </p>
        </motion.div>
        
        <motion.div
          className="flex flex-col sm:flex-row gap-4 justify-center"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.6 }}
        >
          <motion.a
            href="/business-cases"
            className="inline-flex items-center gap-2 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white px-8 py-4 rounded-lg font-semibold text-lg transition-all duration-300 hover:shadow-lg hover:shadow-blue-500/25 hover:scale-105"
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>
            </svg>
            Business Cases
          </motion.a>
          <motion.a
            href="/bi"
            className="inline-flex items-center gap-2 border border-gray-600 text-gray-300 hover:text-white hover:border-gray-500 px-8 py-4 rounded-lg font-semibold text-lg transition-all duration-300 hover:bg-white/5"
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
            </svg>
            Data & BI
          </motion.a>
        </motion.div>
      </div>
      
      {/* Floating elements */}
      <motion.div
        className="absolute top-20 right-20 w-4 h-4 bg-purple-400 rounded-full opacity-60"
        animate={{
          y: [0, -20, 0],
          opacity: [0.6, 1, 0.6],
        }}
        transition={{
          duration: 3,
          repeat: Infinity,
          ease: "easeInOut"
        }}
      />
      <motion.div
        className="absolute bottom-20 left-20 w-6 h-6 bg-blue-400 rounded-full opacity-60"
        animate={{
          y: [0, 20, 0],
          opacity: [0.6, 1, 0.6],
        }}
        transition={{
          duration: 4,
          repeat: Infinity,
          ease: "easeInOut",
          delay: 1
        }}
      />
    </section>
  );
};

export default HeroSection;
