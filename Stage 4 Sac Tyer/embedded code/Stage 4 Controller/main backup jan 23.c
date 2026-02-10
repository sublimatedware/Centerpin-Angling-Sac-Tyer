/* Holy shit this is too much fucking shit fuck me
 * Jacob Lamoureux and 🅱️eter Maragos
 * Pending Copyright Centerpin Angling 2025
 */
#include "main.h"
#include "usb_device.h"
#include "usbd_cdc_if.h"

void SystemClock_Config(void);
static void MX_GPIO_Init(void);

uint8_t RxBuffer[128];
uint8_t connectionEstablished = 0;
uint8_t messageSent = 0;
uint8_t connectionHandshake[] = {'l','m','a','o'};
uint8_t buttonPress[] = {'b','u','t','t','\n'};
uint8_t buttonUnPress[] = {'a','s','s','\n'};

int main(void)
{
  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();
  /* Configure the system clock */
  SystemClock_Config();
  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_USB_DEVICE_Init();

  while (1)
  {
	  if ((HAL_GPIO_ReadPin(GPIOA, GPIO_PIN_0) == 0) && connectionEstablished == 1 )
	  {
		  //HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);		//toggle LED
		  CDC_Transmit_FS(&buttonPress, 5);

		  // wait a third of a second, Kevin Visser-Weckworths Perfect time interval
	  }
	  else if ((HAL_GPIO_ReadPin(GPIOA, GPIO_PIN_0) == 1) && connectionEstablished == 1 )
	  {
		 CDC_Transmit_FS(&buttonUnPress, 4);

		 // HAL_GPIO_WritePin(GPIOC, GPIO_PIN_13, 1);
	  }

	  if((RxBuffer[0] == 97) && (RxBuffer[1] == 98) && (RxBuffer[2] == 97))				//aba turn light off
	  {
		  //HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);		//toggle LED
		  HAL_GPIO_WritePin(GPIOC, GPIO_PIN_13, 1);
	  }
	  else if((RxBuffer[0] == 98) && (RxBuffer[1] == 97) && (RxBuffer[2] == 98))		//bab turn light on
	  {
		  HAL_GPIO_WritePin(GPIOC, GPIO_PIN_13, 0);
	  }

	  if((RxBuffer[0] == 97) && (RxBuffer[1] == 121) && (RxBuffer[2] == 121))			//ayy lmao
	  {
		  CDC_Transmit_FS(&connectionHandshake, 5);
		  connectionEstablished = 1;
	  }
  }
}

void USB_RXCallBack(uint8_t* Buf, uint32_t* Len)
{
	memcpy(RxBuffer, Buf, *Len);
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1);

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLM = 25;
  RCC_OscInitStruct.PLL.PLLN = 192;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV2;
  RCC_OscInitStruct.PLL.PLLQ = 4;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_3) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};
/* USER CODE BEGIN MX_GPIO_Init_1 */
/* USER CODE END MX_GPIO_Init_1 */

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOC_CLK_ENABLE();
  __HAL_RCC_GPIOH_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOC, GPIO_PIN_13, GPIO_PIN_RESET);

  /*Configure GPIO pin : PC13 */
  GPIO_InitStruct.Pin = GPIO_PIN_13;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

  /*Configure GPIO pin : PA0 */
  GPIO_InitStruct.Pin = GPIO_PIN_0;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_PULLUP;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

/* USER CODE BEGIN MX_GPIO_Init_2 */
/* USER CODE END MX_GPIO_Init_2 */
}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
