
import React, { useState } from 'react';
import { BarChart, LineChart, Wallet, Leaf, Home, User, Trees, Droplets, Wind, AlertCircle, ArrowUpRight } from 'lucide-react';

export default function GreenImpactApp() {
  const [activeTab, setActiveTab] = useState('home');
  
  // Sample data
  const accountBalance = 12578.45;
  const savingsGoal = 15000;
  const interestRate = 3.5;
  const co2Saved = 487;
  const treesPlanted = 32;
  const waterSaved = 14752;
  const renewableEnergy = 658;
  
  // Recent transactions
  const transactions = [
    { id: 1, date: 'Apr 7', description: 'Deposit', amount: 500, category: 'Income' },
    { id: 2, date: 'Apr 5', description: 'Solar Panel Project', amount: -200, category: 'Investment' },
    { id: 3, date: 'Apr 2', description: 'Interest Payment', amount: 36.45, category: 'Interest' },
    { id: 4, date: 'Mar 28', description: 'Reforestation Fund', amount: -150, category: 'Investment' }
  ];
  
  // Project allocation
  const projectAllocation = [
    { name: 'Renewable Energy', percentage: 45, color: 'bg-green-500' },
    { name: 'Reforestation', percentage: 25, color: 'bg-emerald-500' },
    { name: 'Clean Water', percentage: 20, color: 'bg-blue-500' },
    { name: 'Sustainable Agriculture', percentage: 10, color: 'bg-yellow-500' }
  ];

  return (
    <div className="flex flex-col h-screen bg-gray-50">
      {/* Status Bar */}
      <div className="bg-green-600 text-white p-2 flex justify-between items-center text-xs">
        <div>9:41 AM</div>
        <div className="flex space-x-2">
          <div>5G</div>
          <div>100%</div>
        </div>
      </div>
      
      {/* App Header */}
      <header className="bg-green-600 text-white p-4 pb-6 rounded-b-xl">
        <div className="flex justify-between items-center">
          <h1 className="text-xl font-bold flex items-center">
            <Leaf className="mr-2" size={20} />
            Green Impact
          </h1>
          <div className="flex space-x-4">
            <AlertCircle size={20} />
            <User size={20} />
          </div>
        </div>
      </header>
      
      {/* Main Content */}
      <main className="flex-1 overflow-auto px-4 pt-2 pb-20">
        {/* content truncated for brevity */}
      </main>
      
      {/* Bottom Navigation */}
      <nav className="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 flex justify-around py-2">
        <button 
          className={`flex flex-col items-center p-2 ${activeTab === 'home' ? 'text-green-600' : 'text-gray-500'}`}
          onClick={() => setActiveTab('home')}
        >
          <Home size={20} />
          <span className="text-xs mt-1">Home</span>
        </button>
        <button 
          className={`flex flex-col items-center p-2 ${activeTab === 'impact' ? 'text-green-600' : 'text-gray-500'}`}
          onClick={() => setActiveTab('impact')}
        >
          <BarChart size={20} />
          <span className="text-xs mt-1">Impact</span>
        </button>
        <button 
          className={`flex flex-col items-center p-2 ${activeTab === 'invest' ? 'text-green-600' : 'text-gray-500'}`}
          onClick={() => setActiveTab('invest')}
        >
          <LineChart size={20} />
          <span className="text-xs mt-1">Invest</span>
        </button>
        <button 
          className={`flex flex-col items-center p-2 ${activeTab === 'account' ? 'text-green-600' : 'text-gray-500'}`}
          onClick={() => setActiveTab('account')}
        >
          <User size={20} />
          <span className="text-xs mt-1">Account</span>
        </button>
      </nav>
    </div>
  );
}
